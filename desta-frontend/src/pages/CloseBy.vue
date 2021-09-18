<template>
    <div class="ui grid">
        <div class="six wide column red">
                <form class="ui segment large form">
                    <div class="ui message red" v-show="error">{{error}}</div>
                    <div class="ui segment">
                        <div class="field">
                            <div class="ui right icon input large" :class="{loading:spinner}">
                                <input type="text" placeholder="Enter your address" v-model = "address" ref="autocomplete"/>
                                <i class="location arrow link icon" @click="locatorButtonPressed"></i>
                            </div>
                        </div>
                        <div class="field">
                            <div class="two fields">
                                <div class="field">
                                    <select v-model="type">
                                        <option value="restaurant"> Restaurant </option>
                                    </select>

                                </div>
                                <div class="field">
                                    <select v-model="radius">
                                        <option value="5"> 5km </option>
                                        <option value="10"> 10km </option>
                                        <option value="15"> 15km </option>
                                        <option value="20"> 20km </option>
                                    </select>                                 
                                </div>
                            </div>
                        </div>
                    <button class="ui button" @click="exploreButtonClicked">Explore</button>
                    </div>
                </form>
                <div class="ui segment" style="max-height:350px;overflow:auto"> 
                    <div class="ui divided items" >
                    <div class="item" v-for="(place, index) in places" :key="place.place_id" @click="showInfoWindow(index)" 
                    :class="{'active' : activeIndex === index}"
                    style="padding:10px">
                        <div class="content">
                            <div class="header">{{place.name}}</div>
                            <div class="meta">{{place.vicinity}}</div>
                        </div>
                    </div>
                    </div>
                </div>
        </div>
        <div class="ten wide column" ref="map">    
        </div>
    </div>
</template>>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            address : "",
            error : "",
            spinner : false,
            apiKey : "AIzaSyB3IgBtYB_flI-c_krmG7CDyaYQHoxV-6U",
            lat : 0,
            lng : 0,
            type : "",
            radius : "",
            places : [],
            markers : [],
            activeIndex : -1
        };  
    },
    mounted() { //called when the DOM is ready
        //instantiate autocomplete object
        let autocomplete = new google.maps.places.Autocomplete(
            this.$refs["autocomplete"], 
            {
                bounds : new google.maps.LatLngBounds(
                    new google.maps.LatLng(45.508888, -73.561668)
                )
            }
        );
        //autocomplete event listener - event, callback
        autocomplete.addListener("place_changed", () => {
            let place = autocomplete.getPlace();
            this.address = place.formatted_address;
            this.lat = place.geometry.location.lat();
            this.lng = place.geometry.location.lng();
        });
    },
    methods: {
            locatorButtonPressed () {
                this.spinner = true;
                if(navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(position => {
                        this.lat = position.coords.latitude;
                        this.lng = position.coords.longitude;
                            this.getAddressFrom(
                                position.coords.latitude, 
                                position.coords.longitude
                            );
                            // this.showUserLocationOnTheMap(
                            //     position.coords.latitude, 
                            //     position.coords.longitude
                            // );
                        }, error => {
                            this.error = error.message;
                            this.spinner = false;
                        }
                    )
                } else {    
                    this.error = "Your browser does not suppoort geolocation API";
                    this.spinner = false;
                }
            }, 
            getAddressFrom(lat,long) { 
                axios.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+ 
                lat + 
                ',' + 
                long + 
                "&key=" + this.apiKey)
                .then((response) => {
                    if(response.data.error_message) {
                        this.error = response.data.error_message; 
                    } else {
                        this.address = response.data.results[0].formatted_address;
                    }
                    this.spinner = false;
                })
                .catch((error) => {
                    this.error = error.message;
                    this.spinner = false;
                })
            },
            exploreButtonClicked() {
                const URL = `https://cors-anywhere.herokuapp.com/https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=${
                    this.lat
                },${this.lng}&type=${this.type}&radius=${this.radius * 1000}&key=${
                    this.apiKey
                }`;

                axios.get(URL).then(response => {
                    this.places = response.data.results;
                    this.showPlacesOnMap();
                }).catch(error => {
                    this.error = error.message;
                })
            },
            showPlacesOnMap() {
                const map = new google.maps.Map(this.$refs["map"], {
                    zoom: 15,
                    center: new google.maps.LatLng(this.lat, this.lng),
                    mapTypeId: google.maps.MapTypeId.ROADMAP
                });
                //popup window
                const infoWindow = new google.maps.InfoWindow();
                //loop places, add marker
                for(let i = 0; i < this.places.length; i++) {
                    const lat = this.places[i].geometry.location.lat;
                    const lng = this.places[i].geometry.location.lng;
                    const placeID = this.places[i].place_id;

                    const marker = new google.maps.Marker({
                        position : new google.maps.LatLng(lat, lng),
                        map : map,
                    });
                    
                    this.markers.push(marker);
                    //object, action, callback
                    google.maps.event.addListener(
                        marker,
                        "click",
                        () => {
                            //http req to place details API
                            const URL = `https://cors-anywhere.herokuapp.com/https://maps.googleapis.com/maps/api/place/details/json?key=${this.apiKey}&place_id=${placeID}`;

                            axios.get(URL)
                            .then(response => {
                                if(response.data.error_message) {
                                    this.error = response.data.error_message;
                                } else {
                                    const place = response.data.result;
                                    console.log(place);
                                    
                                    infoWindow.setContent(`<div class="ui header">${place.name}</div>
                                        ${place.formatted_address} <br/>
                                        ${place.formatted_phone_number} <br/>
                                        <a href="${place.website}" targer="_blank">${place.website}</a>
                                        `
                                    );
                                    infoWindow.open(map, marker); //map and market to add infoWindow
                                }   
                            })
                            .catch(error => {
                                this.error = error.message;
                            })
                        }
                    );
                }

            },
            showInfoWindow(index) {
                this.activeIndex = index;
                new google.maps.event.trigger(this.markers[index], "click");
            }
    },
};
</script>

<style>
    .ui.button, 
    .dot.circle.icon {
        background-color: #ff5a5f;
        color: white;
    }
    
    .pac-icon {
        display : none
    }
    
    .pac-item {
        padding : 10px;
        font-size : 16px;
        cursor: pointer;
    }

    .pac-item:hover {
        background-color : #ececee
    }

    .pac-item-query {
        font-size : 16px;
    }

    .active {
        background: #bef0ed !important;
    }
    
</style>
