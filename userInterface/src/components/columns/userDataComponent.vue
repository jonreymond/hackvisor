 <script setup>
import Client_data from '../../Client_Data.json'
</script>
<template>
    <div>
        <table class="table table-striped table-hover">
            <thead>
                <tr>
                    <th v-for="(key, index) in Object.keys(data[0])" :key="index">
                        <div id="headerCell">
                            {{ key }}
                            <select v-if="key != 'Value' && key != 'Notes'" v-model="filters[key]" class="form-select">
                                <option :value=null>All</option>
                                <option v-for="(value, index) in [...new Set(data.map(e => e[key]))].sort()"
                                    :key="index" :value="value">
                                    {{ value }}
                                </option>
                            </select>
                            <div v-if="key == 'Value' || key == 'Notes'" style="visibility: hidden; height : 35px; "></div>
                        </div>
                    </th>
                </tr>
            </thead>
        </table>
        <div class="table-container">
            <table class="table table-striped table-hover">
                <tbody>
                    <tr v-for="(value, index) in computedData" :key="index">
                        <template v-for="(val, i) in value">
                            <td>
                                <input type="text" v-if="i == 'Notes'" @input="updateData(index, i, $event.target.value)">
                                <p v-if="i != 'Notes'">{{ val }}</p>
                            </td>
                        </template>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script>
export default {
    name: "userDataComponent",
    data() {
        return {
            data: Object.values(Client_data),
            dataOrg: Object.values(Client_data),
            filters: {
                "Category": null,
                "Field": null,
                "Value": null,
                "Notes": null
            }
        }

    },
    methods: {
        updateData(index, key, value) {
            this.data[index][key] = value;
            this.dataOrg[index][key] = value;
        }
    },
    computed: {
        computedData() {

            if (Object.values(this.filters).every(e => e == null)) {
                return this.data
            } else {
                this.data = this.dataOrg
                return this.data.filter(item => {
                    return Object.entries(this.filters).every(([f, v]) => {
                        if (v != null) {
                            return item[f] == v
                        } else return true
                    })
                })
            }
        }
    }

};  
</script>
<style scoped>
.table {
    border-collapse: collapse;
}

.table thead {
    position: sticky;
    top: 0;
    background-color: grey;
    z-index: 1;
    text-align: center
}

.table-container {
    max-height: 60vh;
    overflow-y: scroll;
    width: 100%;
}

.table td, .table th {
    width: 300px;
}

select {
    width: 250px;
    text-align: center;
}


.headerCell {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    text-align: center;

}
</style>