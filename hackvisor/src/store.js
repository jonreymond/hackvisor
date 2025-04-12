import { defineStore } from 'pinia'

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
        getFirstProducts(n) 
        {
            return this.products.slice(0, n);
        }
    }

})

export const useUserStore = defineStore('user', {
    state: () => ({
        user: {
            "clientId": "C123456789",
            "personalInfo": {
                "firstName": "Jane",
                "lastName": "Doe",
                "dateOfBirth": "1985-07-12",
                "email": "jane.doe@example.com",
                "phone": "+1-555-123-4567",
                "address": {
                    "street": "123 Main Street",
                    "city": "Springfield",
                    "state": "IL",
                    "postalCode": "62704",
                    "country": "USA"
                }
            },
            "accounts": [
                {
                    "accountId": "A1001",
                    "type": "Checking",
                    "balance": 2530.75,
                    "currency": "USD",
                    "openedDate": "2020-01-15",
                    "isPrimary": true
                },
                {
                    "accountId": "A1002",
                    "type": "Savings",
                    "balance": 10234.89,
                    "currency": "USD",
                    "openedDate": "2019-11-03",
                    "interestRate": 0.02
                }
            ],
            "creditCards": [
                {
                    "cardId": "CC7890",
                    "cardType": "Visa Platinum",
                    "limit": 5000,
                    "balance": 1234.56,
                    "dueDate": "2025-05-05",
                    "status": "Active"
                }
            ],
            "loans": [
                {
                    "loanId": "L3456",
                    "type": "Auto Loan",
                    "principal": 15000,
                    "outstanding": 6200.50,
                    "monthlyPayment": 320.75,
                    "startDate": "2021-03-10",
                    "endDate": "2026-03-10",
                    "interestRate": 0.045
                }
            ],
            "preferences": {
                "language": "en",
                "communication": {
                    "email": true,
                    "sms": false,
                    "phone": false
                },
                "marketingOptIn": true
            },
            "kycStatus": "Verified",
            "lastLogin": "2025-04-12T08:45:00Z",
            "createdAt": "2018-06-22T10:00:00Z"
        }
    }),
    getters: {
        getUser: (state) => state.user
    },
})