<template>
  <div>
    <b-container>
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

                <b-form-group>
                  <b-button type="submit" variant="outline-primary" :disabled="acceptableSubmission">Login</b-button>
                </b-form-group>

              </b-form>
            </b-card-text>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>