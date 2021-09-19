<template >
  <div class='' id='business_registration'  >
    <div class="flex flex-col items-center justify-center bg-gray-800 h-screen select-none">
    <div class="flex flex-col bg-white px-4 sm:px-6 md:px-8 lg:px-10 py-4 rounded-xl shadow-2xl w-full max-w-md  border-l-4 border-blue-900">
        <div class="font-medium self-center text-xl sm:text-2xl uppercase w-30 text-center text-blue-900 rounded-full p-6 ">Register</div>
        <div class="mt-4">
            <form action="" autocomplete="">
                <div class="relative w-full mb-3">
                    <input type="email" v-model = "email" name="email" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Email" style="transition: all 0.15s ease 0s;" />
                </div>
                <div class="relative w-full mb-3">
                    <input type="password" v-model= "password" name="password" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Password" style="transition: all 0.15s ease 0s;" />

                </div>
                <div class="relative w-full mb-3">
                    <input type="password" v-model = 'cpassword' name="cpassword" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Confirm Password" style="transition: all 0.15s ease 0s;" />

                </div>
                <div class="relative w-full mb-3">
                    <input type="text" v-model = 'business_name' name="business_name" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Business name" style="transition: all 0.15s ease 0s;" />

                </div>
                <div class="relative w-full mb-3">
                    <input type="tel" v-model="phone_number" name="phone_number" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Phone Number" style="transition: all 0.15s ease 0s;" />

                </div>
                <div class="relative w-full mb-3">
                    <input type="tel" name="website_link" v-model = "website_link" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Website Link" style="transition: all 0.15s ease 0s;" />

                </div>
                <div class="relative w-full mb-3">
                    <input type="tel" name="instagram_link" v-model = "instagram_link" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Instagram Link" style="transition: all 0.15s ease 0s;" />

                </div>
                <div class="text-center mt-6">
                    <input type="button" name="signin" @click="createBusiness(email, password, cpassword, business_name, phone_number, website_link, instagram_link)" id="signin" value="Sign In" class="p-3 rounded-full bg-blue-900 outline-none text-white shadow w-32 justify-center focus:bg-purple-700 hover:bg-purple-500">
                </div>
                <div class="flex flex-wrap mt-6">
                    <div class="w-1/2 text-left">
                        <a href="#" class="text-blue-900 text-xl" @click="openLoginPage"><small>Already a member? Login</small></a>
                    </div>
                    <!-- <div class="w-1/2 text-right">
                        <a href="#" class="text-blue-900 text-xl rounded-lg"><small>Sign In</small></a>
                    </div> -->
                </div>
            </form>
<span v-if="errorBusiness" style="color:red">Error: {{errorBusiness}} </span>
<span v-if="message" style="color:green">Message: {{message}} </span>
        </div>
    </div>
  </div>

  </div>
</template>

<script>

import axios from 'axios'

var config = require('../../config')

var frontendUrl = 'http://' + config.dev.host + ':' + config.dev.port
var backendUrl = 'http://' + config.dev.backendHost + ':' + config.dev.backendPort

var AXIOS = axios.create({
  baseURL: backendUrl,
  headers: { 'Access-Control-Allow-Origin': frontendUrl }
})


export default {
  name: 'business_registration',
  data() {
    return {
      email:"",
      errorBusiness: 'We are here',
      message :""
    }
  },
  created: function () {},
  methods: {
    createBusiness: function(email, password, cpassword, business_name, phone_number, website_link, instagram_link) {
      if(password != cpassword){
        this.errorBusiness = "Passwords do not match"
        this.message = ""
      } else {
        const business_details = {'email':email, 'password':password, "name":business_name,
        'phone_no': phone_number, 'website':website_link , 'instagram':instagram_link};
        AXIOS.post('/register_business', {business_details}, {}).then(response =>{
              this.message = response.data.message
              this.email='', this.password='', this.cpassword='', this.business_name='', this.phone_number='', this.website_link='', this.instagram_link=''
              alert("You have successfully created your account! now I will take you to the profile page.")
              this.$router.push('/profile')
          }).catch(e =>{
              this.errorBusiness = e.data.message
              console.log(e.data.message)
              console.log(500)
          })
      }
    }


  }


}

</script>
