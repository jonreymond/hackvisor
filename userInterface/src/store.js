import { defineStore } from 'pinia'
import clientDataJson from './Client_Data.json'


export const graphStore = defineStore('graph', {

})


export const useProductStore = defineStore('product', {

    state: () => ({
        products: [
            { id: 1, name: "Checking Accounts" },
            { id: 2, name: "Savings Accounts" },
            { id: 3, name: "Credit Cards" },
            { id: 4, name: "Personal Loans" },
            { id: 5, name: "Mortgages" },
            { id: 6, name: "Auto Loans" },
            { id: 7, name: "Business Accounts & Loans" },
            { id: 8, name: "Certificates of Deposit (CDs)" },
            { id: 9, name: "Investment Services" },
            { id: 10, name: "Insurance Products" }
        ],
        selectedProduct: { name: null, id: null },
    }),
    getters: {
        getProducts: (state) => state.products,
        getSelectedProduct: (state) => state.selectedProduct,
    },
    actions: {
        getFirstProducts(n) {
            return Object.entries(this.products).slice(0, n).map(([k, e]) => {
                e['importance'] = 0
                console.log(k)
                if (k == 1) {
                    e['importance'] = 1
                    return e
                } else return e
            });
        }
    }

})


// go from csv to json 
const csvToJson = (csvFile) => {
    return new Promise((resolve, reject) => {
        Papa.parse(csvFile, {
            header: true,
            skipEmptyLines: true,
            complete: (results) => {
                resolve(results.data);
            },
            error: (error) => {
                reject(error);
            }
        });
    });
};


console.log(clientDataJson)
export const useUserStore = defineStore('user', {
    state: () => ({
        user: Object.values(clientDataJson),
        getters: {
            getUser: (state) => state.user
        },
    })
})