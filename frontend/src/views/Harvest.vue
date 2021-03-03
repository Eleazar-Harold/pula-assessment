<template>
    <div class="harvests">
        <Navbar></Navbar>
        <div class="album py-5 bg-light">
          <div class="container">
            <div class="row">
              <table class="table table-striped table-hover">
                <thead>
                    <tr>
                    <th scope="col">#</th>
                    <th scope="col">Weight</th>
                    <th scope="col">Dry Weight</th>
                    <th scope="col">Farm Name</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="harvest in harvestData" :key="harvest.id" class="col-md-4">
                        <th scope="row"></th>
                        <td>{{harvest.harvest_weight}}</td>
                        <td>{{harvest.dry_weight}}</td>
                        <td>{{harvest.farm.name}}</td>
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
import {mapState} from 'vuex';
export default {
    name: 'Harvests',
    onIdle () {
      this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({ name: 'login' })
        })
    },
    data()  {
        return {
            harvestData: []
        }
    },
    components: {
        Navbar
    },
    computed: mapState(['harvestData']),
    created() {
        api.get('harvest',{headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
        .then(response => {
            console.log('Harvest API has received data')
            this.$store.state.harvestData = response.data
        }).catch(err => {
            console.log(err)
        })
    },
}
</script>

<style scoped>

</style>