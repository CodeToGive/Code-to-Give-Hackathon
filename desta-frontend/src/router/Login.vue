<template>
  <div id="login_page" class="flex flex-col items-center justify-center bg-gray-800 h-screen select-none">
    <div class="flex flex-col -mt-32 bg-white px-4 sm:px-6 md:px-8 lg:px-10 py-8 rounded-xl shadow-2xl w-full max-w-md  border-l-4 border-blue-900">
        <div class="font-medium self-center text-xl sm:text-2xl uppercase w-30 text-center text-blue-900 rounded-full p-6 ">Sign In</div>
        <div class="mt-10">
            <form action="" autocomplete="">
                <div class="relative w-full mb-3">
                    <input v-model="email" type="email" name="email" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Email" style="transition: all 0.15s ease 0s;" />
                    <small class="p-2 text-red-500">* Email</small>
                </div>
                <div class="relative w-full mb-3">
                    <input v-model="password" type="password" name="password" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Password" style="transition: all 0.15s ease 0s;" required/>
                    <small class="p-2 text-red-500">* Password</small>
                </div>
                <div class="text-center mt-6">
                    <input type="button" @click="signIn(email,password)" name="signin" id="signin" value="Sign In" class="p-3 rounded-full bg-blue-900 outline-none text-white shadow w-32 justify-center focus:bg-purple-700 hover:bg-purple-500" required>
                </div>
                <div class="flex flex-wrap mt-6">
                    <div class="w-1/2 text-left">
                        <a href="#" class="text-blue-900 text-xl"><small>Forgot password?</small></a>
                    </div>
                    <div class="w-1/2 text-right">
                        <a href="#" @click="signup" class="text-blue-900 text-xl rounded-lg"><small>Sign up</small></a>
                    </div>
                </div>
            </form>
            <span v-if="errorLog" style="color:red">Error: {{errorLog}} </span>
            <span v-if="msgLog" style="color:green">Message: {{msgLog}} </span>
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
  name: 'login_page',
  data() {
    return {
      email: '', // When user inputs the email, it'll be stored here
      password: '',
      errorLog:'',
      msgLog:""
    }
  },
  methods: {
    signIn: function(email, password){
        if(email==''|| password==""){
          this.errorLog="Email/Password is empty"
          this.msgLog = ''
} else{
         const details = {'email': email, 'password':password}
         AXIOS.post('/login', {details}, {}).then(response =>{
                    this.email='', this.password='', this.cpassword='', this.business_name='', this.phone_number='', this.website_link='', this.instagram_link=''
                    this.msgLog="You are logged in!"
                    this.errorLog=''
                }).catch(e =>{
                    this.errorLog = e.response.data.message
                    this.msgLog = ''
                    this.email='', this.password=''
                })

}



},
    signup() {
      alert("Going to the signup page!")
      this.$router.push('/registration')
    }
  }
}


</script>
