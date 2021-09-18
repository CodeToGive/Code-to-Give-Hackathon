<template>
    <div>
        <section class="ui two column centered grid" style="position:relative;z-index:1;"> 
            <div class="column">
                <form class="ui segment large form">
                    <div class="ui message red" v-show="error">{{error}}</div>
                    <div class="ui segment">
                    <div class="field">
                        <div class="ui right icon input large" :class="{loading:spinner}">
                            <input type="text" placeholder="Enter your address" v-model = "address" ref="autocomplete"/>
                            <i class="location arrow link icon" @click="locatorButtonPressed"></i>
                        </div>
                    </div>
                    <button class="ui button">Go!</button>
                    </div>
                </form>
                </div>
            
        </section>

        <section id="map">
        </section>
    </div> 
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            address : "",
            error : "",
            spinner : false
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
            this.showUserLocationOnTheMap(place.geometry.location.lat(), place.geometry.location.lng())
        });
        
    },
    methods: {
            locatorButtonPressed () {
                this.spinner = true;
                if(navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(position => {
                            this.getAddressFrom(
                                position.coords.latitude, 
                                position.coords.longitude
                            );
                            this.showUserLocationOnTheMap(
                                position.coords.latitude, 
                                position.coords.longitude
                            );
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
                "&key=AIzaSyB3IgBtYB_flI-c_krmG7CDyaYQHoxV-6U")
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
            showUserLocationOnTheMap(latitude, longitude) {
                //create a map object
                let map = new google.maps.Map(document.getElementById("map"), {
                    zoom : 15,
                    center : new google.maps.LatLng(latitude, longitude),
                    mapTypeId : google.maps.MapTypeId.ROADMAP
                });
                //define marker
                new google.maps.Marker({
                    position : new google.maps.LatLng(latitude, longitude),
                    map : map
                })
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

    #map {
        position: absolute;
        top:0;
        bottom: 0;
        left: 0;
        right: 0;
        background-color : teal
    }

</style>