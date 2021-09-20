<template>
  <div class="min-h-screen p-6 bg-gray-100 flex items-center justify-center">
    <div class="container max-w-screen-lg mx-auto flex justify-center items-center">
      <div class="">
        <h2 class="font-semibold text-xl text-gray-600">Your account details</h2>
        <div class=" flex justify-center items-center bg-white rounded shadow-lg p-4 px-4 md:p-8 mb-6">
          <div class="grid gap-4 gap-y-2 text-sm grid-cols-1 lg:grid-cols-3">
            <div class="lg:col-span-2">
              <div class="grid gap-4 gap-y-2 text-sm grid-cols-1 md:grid-cols-5">
                <div class="md:col-span-3">
                  <label for="full_name">Business name</label>
                  <input v-model='name' type="text" name="full_name" id="full_name" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50" value="" />
                </div>

                <div class="md:col-span-3">
                  <label for="email">Email Address</label>
                  <input v-model='email' type="text" name="email" id="email" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50" value="" placeholder="email@domain.com" />
                </div>

                <div class="md:col-span-3">
                  <label for="address">Business Address</label>
                  <input v-model="location" type="text" name="address" id="address" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50" value="" placeholder="" />
                </div>

                <div class="md:col-span-3">
                  <label for="address">Phone number</label>
                  <input v-model='phone_number' type="text" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50" value="" placeholder="" />
                </div>

                <div class="md:col-span-3">
                  <label for="address">Website</label>
                  <input v-model='websiteLink' type="text" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50" value="" placeholder="" />
                </div>

                <div class="md:col-span-3">
                  <label for="address">Business Description</label>
                  <textarea v-model='tag' type="text" rows="5" cols="50" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50" value="" placeholder="Write a short description of your business" />
                </div>

                <div class="md:col-span-3">
                  <label for="address">Category</label>
                  <input v-model='tag' type="text" class="h-10 border mt-1 rounded px-4 w-full bg-gray-50" value="" placeholder="" />
                </div>

                <div class="md:col-span-3 text-right">
                  <div class="inline-flex items-end">

                    <button @click='saveChanges' class="bg-yellow-500 hover:bg-black text-white font-bold py-2 px-6 rounded-lg">Submit</button>
                  </div>
                </div>

              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

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
  props: ['user'],
  data() {
    return { //TODO this will be where we get the restaurant object and pass the data to dynamically populate this page
      name: '',
      tag: '',
      location: '',
      about: '',
      websiteLink: '',
      email: '',
      phone_number: '',
      errorProf: ''

    }
  },
  methods: {
    saveChanges() {
      // TODO DO A POST REQUEST HERE
      alert("This is just to see if we can get the data from the input: " + this.name + this.tag + this.location)
      this.$router.push('/OwnerProfile')
    }
  },
  created() {
    // TODO DO A GET DATA REQUEST HERE
    this.name = 'Jerk Chicken Montreal',
    this.tag = 'Restaurant',
    this.location = 'Montreal, QC'
    this.websiteLink = 'hellothere.com'
    this.email = response.data.email
    this.about = 'We are family run business and we make the best chicken in the world! We are family run business and we make the best chicken in the world! We are family run business and we make the best chicken in the world! We are family run business and we make the best chicken in the world! We are family run business and we make the best chicken in the world! We are family run business and we make the best chicken in the world! We are family run business and we make the best chicken in the world!We are family run business and we make the best chicken in the world! We are family run business and we make the best chicken in the world!',
    this.email = 'bestjerkchicken@gmail.com',
    this.phone_number= '437588077'

    // this.email = 'desta@org'
    // AXIOS.get('/business_details/', {
    //   params: {
    //     email: this.email
    //   }
    // }).then(response => {
    //     this.name = response.data.name,
    //     this.tag = response.data.tag,
    //     this.location = response.data.address + " " + response.data.postal_code
    //     this.about = response.data.description
    //     this.websiteLink = response.data.website
    //     this.email = response.data.email
    //     this.phone_number = response.data.phone_number
    // })
    //   .catch(e => {
    //     console.log(e.response.data.message)
    //     errorProf = e.response.data.message
    //   })
  },
  updated() {
  },
  destroyed() {
  },
  mounted() {
  }
}
</script>
