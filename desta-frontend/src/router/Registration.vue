<template>
  <div class="">
    <div class="flex flex-col items-center justify-center bg-gray-800 h-screen select-none">
    <div class="flex flex-col bg-white px-4 sm:px-6 md:px-8 lg:px-10 py-4 rounded-xl shadow-2xl w-full max-w-md  border-l-4 border-blue-900">
        <div class="font-medium self-center text-xl sm:text-2xl uppercase w-30 text-center text-blue-900 rounded-full p-6 ">Register</div>
        <div class="mt-4">
            <form method="POST" action="" autocomplete="">
                <div class="relative w-full mb-3">
                    <input v-model="email" type="email" name="email" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Email" style="transition: all 0.15s ease 0s;" />
                </div>
                <div class="relative w-full mb-3">
                    <input v-model="password" type="password" name="password" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Password" style="transition: all 0.15s ease 0s;" />

                </div>
                <div class="relative w-full mb-3">
                    <input v-model="confirmpassword" type="password" name="cpassword" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Confirm Password" style="transition: all 0.15s ease 0s;" />

                </div>
                <div class="relative w-full mb-3">
                    <input v-model="business_name" type="text" name="business_name" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Business name" style="transition: all 0.15s ease 0s;" />
                </div>
                <div class="relative w-full mb-3">
                    <input v-model="number" type="tel" name="phone_number" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Phone Number" style="transition: all 0.15s ease 0s;" />
                </div>
                <div class="relative w-full mb-3">
                    <input v-model="link" type="tel" name="website_link" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Website Link" style="transition: all 0.15s ease 0s;" />
                </div>
                <div class="relative w-full mb-3">
                    <input v-model="instagram_link" type="tel" name="instagram_link" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Instagram Link" style="transition: all 0.15s ease 0s;" />
                </div>
                <div class="text-center mt-6">
                    <input @submit="createNewAccount" type="submit" name="signin" id="signin" value="Sign In" class="p-3 rounded-full bg-blue-900 outline-none text-white shadow w-32 justify-center focus:bg-purple-700 hover:bg-purple-500">
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
        </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  data() {
    return {
      email: '', // When user inputs the email, it'll be stored here
      password: '',
      confirmpassword: '',
      business_name: '',
      number: '',
      link: '',
      instagram_link: '',
    }
  },
  methods: {
    createNewAccount() {
      //make post request here
    },
    openLoginPage() {
      this.$router.push('/Login')
    }
  }
}

</script>
