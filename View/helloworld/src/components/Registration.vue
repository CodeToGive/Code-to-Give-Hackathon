<template>
  <div>
    <b-container>
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
    </b-container>
  </div>
</template>