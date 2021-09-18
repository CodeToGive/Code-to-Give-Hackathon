<template>
  <div class="flex flex-col items-center justify-center bg-gray-800 h-screen select-none">
    <div class="flex flex-col -mt-32 bg-white px-4 sm:px-6 md:px-8 lg:px-10 py-8 rounded-xl shadow-2xl w-full max-w-md  border-l-4 border-blue-900">
        <div class="font-medium self-center text-xl sm:text-2xl uppercase w-30 text-center text-blue-900 rounded-full p-6 ">Sign In</div>
        <div class="mt-10">
            <form method="POST" action="" autocomplete="">                
                <div class="relative w-full mb-3">
                    <input type="email" name="email" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Email" style="transition: all 0.15s ease 0s;" />
                    <small class="p-2 text-red-500">* Email</small>
                </div>
                <div class="relative w-full mb-3">
                    <input type="password" name="password" class="border-2 p-2 placeholder-gray-400 text-gray-700 bg-white rounded text-sm  focus:outline-none focus:ring w-full" placeholder="Password" style="transition: all 0.15s ease 0s;" />
                    <small class="p-2 text-red-500">* Password</small>
                </div>
                <div class="text-center mt-6">
                    <input type="submit" name="signin" id="signin" value="Sign In" class="p-3 rounded-full bg-blue-900 outline-none text-white shadow w-32 justify-center focus:bg-purple-700 hover:bg-purple-500">
                </div>  
                <div class="flex flex-wrap mt-6">
                    <div class="w-1/2 text-left">
                        <a href="#" class="text-blue-900 text-xl"><small>Forgot password?</small></a>
                    </div>
                    <div class="w-1/2 text-right">
                        <a href="#" class="text-blue-900 text-xl rounded-lg"><small>Sign In</small></a>
                    </div>
                </div>
            </form>
        </div>
    </div>
  </div>
    
    <!-- <b-container>
      <b-row class="justify-content-md-center mt-4" >
        <b-col col md="8">
          <b-card
              header="Login into your account"
              header-bg-variant="primary"
              header-text-variant="white"
          >
            <b-card-text>
              <b-form @submit="onSubmit">

                <b-form-group
                    description="Enter your email"
                    label="Email" >
                  <b-form-input v-model="email" required />
                </b-form-group>

                <b-form-group
                    description="Enter your password"
                    label="Password" >
                  <b-form-input v-model="password" type="password" required />
                </b-form-group>

                <b-form-group >
                  <b-button class="bg-blue-700" type="submit" variant="outline-primary" :disabled="acceptableSubmission">Login</b-button>
                </b-form-group>

              </b-form>
            </b-card-text>
          </b-card>
        </b-col>
      </b-row>
    </b-container> -->
  

 
</template>
