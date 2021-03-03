<template>
    <div class="farms">
        <Navbar></Navbar>
        <div class="album py-5 bg-light">
          <div class="container">
            <div class="row">
              <table class="table table-striped table-hover">
                <thead>
                    <tr>
                    <th scope="col">#</th>
                    <th scope="col">Name</th>
                    <th scope="col">Crop</th>
                    <th scope="col">Size</th>
                    <th scope="col">Town</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="farm in ApiData" :key="farm.id" class="col-md-4">
                        <th scope="row"></th>
                        <td>{{farm.name}}</td>
                        <td>{{farm.crop}}</td>
                        <td>{{farm.size}}</td>
                        <td>{{farm.town}}</td>
                    </tr>
                </tbody>
                </table>
            </div>
          </div>
      </div>
    </div>
</template>

<script>
import { api } from '../axios.api';
import Navbar from '../components/Navbar';
// import {mapState} from 'vuex';
export default {
    name: 'Farms',
    onIdle () {
      this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({ name: 'login' })
        })
    },
    data()  {
        return {
            ApiData: []
        }
    },
    components: {
        Navbar
    },
    // computed: mapState(['ApiData']),
    created() {
        api.get('farm',{headers: {Authorization: `Token ${this.$store.state.accessToken}`}})
        .then(response => {
            console.log('Farm API has received data')
            this.$store.state.ApiData = response.data
        }).catch(err => {
            console.log(err)
        })
    },
}
</script>

<style scoped>

</style>