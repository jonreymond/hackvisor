<template>
    <div id="keyword-component" class="windows">
        <h3>keywordComponent </h3>
        <div class="keyword-cloud" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); gap: 10px;"></div>
        <div class="keyword-cloud">
            <span v-for="keyword in keywords" :key="keyword.word" :style="getKeywordStyle(keyword)"
                @click="selectKeyword(keyword)" class="keyword">
                {{ keyword.word }}
            </span>
        </div>

    </div>
</template>
<script>
export default {
    name: 'KeywordComponent',
    data() {
        return {
            keywords: [
                { "word": "marriage", "related": ["wedding", "honeymoon", "joint account", "family planning"] },
                { "word": "buying a house", "related": ["mortgage", "down payment", "home insurance", "property tax"] },
                { "word": "retirement", "related": ["pension", "401k", "investment", "retirement plan"] },
                { "word": "baby", "related": ["childcare", "savings account", "education fund", "life insurance"] },
                { "word": "divorce", "related": ["child support", "alimony", "separation of assets", "legal fees"] },
                { "word": "inheritance", "related": ["estate planning", "will", "trusts", "inheritance tax"] },
                { "word": "college", "related": ["student loan", "tuition", "scholarships", "education savings plan"] },
                { "word": "health", "related": ["health insurance", "medical bills", "disability insurance", "life insurance"] },
                { "word": "starting a business", "related": ["business loan", "startup capital", "taxes", "small business account"] },
                { "word": "moving", "related": ["relocation loan", "moving expenses", "new job", "cost of living"] },
                { "word": "vacation", "related": ["travel insurance", "savings plan", "credit card rewards", "exchange rate"] },
                { "word": "car purchase", "related": ["auto loan", "insurance", "down payment", "car trade-in"] },
                { "word": "adoption", "related": ["adoption loan", "family support", "education savings", "legal fees"] },
                { "word": "job change", "related": ["salary increase", "severance pay", "tax impact", "job benefits"] },
                { "word": "death of spouse", "related": ["life insurance", "estate planning", "inheritance", "survivor benefits"] },
                { "word": "home renovation", "related": ["home equity loan", "remodeling", "contractor", "personal loan"] },
                { "word": "large gift", "related": ["gift tax", "savings", "bank transfer", "tax planning"] },
                { "word": "graduation", "related": ["student loans", "savings", "career planning", "salary expectations"] },
                { "word": "buying a car", "related": ["auto loan", "insurance", "down payment", "interest rates"] },
                { "word": "funeral expenses", "related": ["life insurance", "estate settlement", "funeral plan", "burial costs"] }
            ]
            ,
            selectedKeyword: null
        }
    },
    methods: {
        selectKeyword(keyword) {
            this.selectedKeyword = keyword;
        },
        getKeywordStyle(keyword) {
            if (!this.selectedKeyword) return {};

            if (keyword.word === this.selectedKeyword.word) {
                return { fontSize: '24px', fontWeight: 'bold', color: '#222' };
            }

            if (this.selectedKeyword.related.includes(keyword.word)) {
                return { fontSize: '18px', fontWeight: '500', color: '#666' };
            }

            return { fontSize: '14px', color: '#aaa' };
        }
    },

    mounted() {
        // Add any initialization code here
    }
}

</script>
<style scoped>
#keyword-component {}

.keyword-cloud {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    cursor: pointer;
}

.keyword {
    transition: all 0.3s ease;
}

.keyword:hover {
    transform: scale(1.1);
    color: #000;
}
</style>