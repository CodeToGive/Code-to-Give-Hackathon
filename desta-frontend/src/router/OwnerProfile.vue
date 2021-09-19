<template>


  <div id="profile_page" class="h-screen flex flex-wrap bg-gray-100 pt-4">
    <div class="flex flex-col w-1/3 h-full px-2">
      <div class="flex inline-block border-2 items-center justify-center rounded-lg h-1/2 w-full">
        <img src="../../build/images/resto1.jpg" alt="No image uploaded" class="object-cover w-full h-full rounded-lg">
      </div>
      <div class="flex inline-block border-2 rounded-lg h-1/2 w-full">
        <img src="../../build/images/resto2.jpg" alt="No image uploaded" class="object-cover w-full h-full rounded-lg">
      </div>
    </div>
    <div class="flex w-2/3 h-full">
      <div class="w-full">
        <div class="border-2 border-gray-300 p-4 shadow-sm rounded-lg mb-4" >
          <div class="flex flex-wrap items-end">
<!--            <input placeholder="desta" />-->
            <div class="text-4xl font-serif font-bold tracking-wide">{{ name }}</div>
            <div class="border-2 rounded-full flex justify-center items-center mx-4 px-2 bg-purple-800 text-white">{{tag}}</div>
          </div>
          <br>
          <div class="text-lg font-serif font-bold mb-4">{{ location }}</div>
          <h4 class="mb-2">About us</h4>
          <div class="text-base">{{ about }}</div>
        </div>

        <div class="border-2 border-gray-300 p-4 shadow-sm rounded-lg mb-4">
          <div class="my-2" >Website:

          </div><span class="text-base font-semibold" contenteditable="true"> {{ websiteLink }}</span>
          <div class="my-2">Email: <span class="text-base font-semibold"> {{ email }}</span></div>
          <div class="">Phone: <span class="text-base font-semibold"> {{ phone_number }}</span></div>
        </div>

        <div class="border-2 border-gray-300 p-4 shadow-sm rounded-lg">
          <div class="text-base my-2 font-semibold">Yelp: <fa icon="star" class="text-yellow-300"></fa><fa icon="star" class="text-yellow-300"></fa></div>
          <!--          <div class="text-base my-2 font-semibold">Yelp <fa icon="star" class="text-yellow-300"></fa>{{ yelpRating }}<fa icon="star" class="text-yellow-300"></fa></div>-->
          <div class="text-base my-2 font-semibold">Google Review:</div>
          <AddGoogleMap />
        </div>
        <b-button id="show-btn" @click="showModal">Open Modal</b-button>

      </div>
    </div>

  </div>


</template>

<script>
export default {
  methods: {
    showModal() {
      this.$refs['my-modal'].show()
    },
    hideModal() {
      this.$refs['my-modal'].hide()
    },
    toggleModal() {
      // We pass the ID of the button that we want to return focus to
      // when the modal has hidden
      this.$refs['my-modal'].toggle('#toggle-btn')
    }
  }
}
</script>




<script>
import axios from 'axios'
import AddGoogleMap from "../pages/AddGoogleMap";
var config = require('../../config')
var frontendUrl = 'http://' + config.dev.host + ':' + config.dev.port
var backendUrl = 'http://' + config.dev.backendHost + ':' + config.dev.backendPort
var AXIOS = axios.create({
  baseURL: backendUrl,
  headers: { 'Access-Control-Allow-Origin': frontendUrl }
})

export default {
  name: "profile_page",
  components: {AddGoogleMap},
  props:['user'],
  data() {
    return { //TODO this will be where we get the restaurant object and pass the data to dynamically populate this page
      name: '',
      tag: '',
      location: '',
      about: '',
      websiteLink: '',
      email: '',
      phone_number: '',
      errorProf:''

    }
  },
  created() {
    this.email = 'desta@org'
    AXIOS.get('/business_details/',{
      params:{
        email: this.email
      }

    }).then(response => {
      console.log(2+5)
      console.log("I am here")
      // JSON responses are automatically parsed.
      console.log(response.data.name)
      this.name = response.data.name,
        this.tag = response.data.tag,
        this.location = response.data.address + " " + response.data.postal_code
      this.about = response.data.description
      this.websiteLink = response.data.website
      //this.email = response.data.email
      this.phone_number = response.data.phone_number
    })
      .catch(e => {
        console.log(e.response.data.message)
        errorProf = e.response.data.message
      })

  },
  updated() {},
  destroyed() {},
  mounted() {
  },
  methods: {
  }
}
</script>
