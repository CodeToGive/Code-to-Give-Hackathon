
<template>
  <div id="app">
<!--    Implement conditional rendering-->
      if (lgoin) {
    <Login />
    }


    <Profile/>
  </div>
</template>



<script>
  import Login from "./components/Login";
  import Profile from "./components/Profile";
  // import Registration from "./components/Registration";
  export default {
    components: {Profile, Login},
    data() {
      return {
      email: '', // When user inputs the email, it'll be stored here
      password: ''
    }
  },
    methods: {
        onSubmit(event) {
          event.preventDefault()
          alert("You are logged in")
          // This is where we will need to make a GET request to the backend to get the data

        }
    },
    computed: {
      acceptableSubmission() { //This form will check if the form is ready to be submitted yet
        return this.email.length > 0 && this.password.length ? false : true
      }
    }
  }
</script>
