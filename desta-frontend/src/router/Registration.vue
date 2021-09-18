<template>
  <div class="">
    <div class="flex flex-col items-center justify-center bg-gray-800 h-screen select-none">
    <div class="flex flex-col bg-white px-4 sm:px-6 md:px-8 lg:px-10 py-4 rounded-xl shadow-2xl w-full max-w-md  border-l-4 border-blue-900">
        <div class="font-medium self-center text-xl sm:text-2xl uppercase w-30 text-center text-blue-900 rounded-full p-6 ">Register</div>
        <div class="mt-4">
            <form method="POST" action="" autocomplete="">
                <div class="relative w-full mb-3">
                    <input type="email" name="email" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Email" style="transition: all 0.15s ease 0s;" />
                </div>
                <div class="relative w-full mb-3">
                    <input type="password" name="password" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Password" style="transition: all 0.15s ease 0s;" />

                </div>
                <div class="relative w-full mb-3">
                    <input type="password" name="cpassword" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Confirm Password" style="transition: all 0.15s ease 0s;" />

                </div>
                <div class="relative w-full mb-3">
                    <input type="text" name="business_name" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Business name" style="transition: all 0.15s ease 0s;" />

                </div>

                <div class="relative w-full mb-3">
                    <input type="tel" name="phone_number" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Phone Number" style="transition: all 0.15s ease 0s;" />

                </div>

                <div class="relative w-full mb-3">
                    <input type="tel" name="website_link" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Website Link" style="transition: all 0.15s ease 0s;" />

                </div>

                <div class="relative w-full mb-3">
                    <input type="tel" name="instagram_link" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Instagram Link" style="transition: all 0.15s ease 0s;" />

                </div>

                <div class="text-center mt-6">
                    <input type="submit" name="signin" id="signin" value="Sign In" class="p-3 rounded-full bg-blue-900 outline-none text-white shadow w-32 justify-center focus:bg-purple-700 hover:bg-purple-500">
                </div>
                <div class="flex flex-wrap mt-6">
                    <div class="w-1/2 text-left">
                        <a href="#" class="text-blue-900 text-xl"><small>Already a member? Login</small></a>
                    </div>
                    <!-- <div class="w-1/2 text-right">
                        <a href="#" class="text-blue-900 text-xl rounded-lg"><small>Sign In</small></a>
                    </div> -->
                </div>
            </form>
        </div>
    </div>
  </div>




      <b-row class="justify-content-md-center mt-4" >
        <b-col col md="8">
          <b-card
              header="Create a new account"
              header-bg-variant="primary"
              header-text-variant="white"
          >
            <b-card-text>
              <b-form @submit="onSubmit">

                <b-form-group
                    label="Account email" >
                  <b-form-input v-model="account_email" required />
                </b-form-group>

                <b-form-group
                    label="Password" >
                  <b-form-input v-model="password" type="password" required />
                </b-form-group>

                <b-form-group
                    label="Renter your password" >
                  <b-form-input v-model="reentered_password" type="password" required />
                </b-form-group>

                <b-form-group
                    label="Business name" >
                  <b-form-input v-model="business_name" required />
                </b-form-group>

                <b-form-group
                    label="Description of your business" >
                  <b-form-input v-model="business_description" type="website_d" required />
                </b-form-group>

                <b-form-group
                    label="Website link" >
                  <b-form-input v-model="website_link" required />
                </b-form-group>

                <b-form-group
                    label="Instagram account" >
                  <b-form-input v-model="instagram_link" required />
                </b-form-group>

                <b-form-group
                    label="Business email address" >
                  <b-form-input v-model="email_address" required />
                </b-form-group>

                <b-form-group label="Phone number" >
                  <b-form-input v-model="phoner_number" required />
                </b-form-group>

                <b-form-group label="Business category">
                    <b-dropdown id="dropdown-1" text="Choose..." class="m-md-2">
                      <b-dropdown-item>Restaurant</b-dropdown-item>
                      <b-dropdown-item>Hair Salon</b-dropdown-item>
                      <b-dropdown-item>Event Planner</b-dropdown-item>
                    </b-dropdown>
                </b-form-group>

                <b-form-group>
                  <b-button type="submit" variant="outline-primary" :disabled="acceptableSubmission">Login</b-button>
                </b-form-group>

              </b-form>
            </b-card-text>
          </b-card>
        </b-col>
      </b-row>
  </div>
</template>

<script>


</script>
