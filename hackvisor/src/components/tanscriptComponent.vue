<script setup>
import dropdownWithSearch from './dropdownWithSearch.vue';
</script>
<template>

    <div id="keyword-component" class="windows">

        <div class="windows-content">
            <div id="transcript">
                <p>This is a black coding-themed window with scrollable text. You can add as much content as you want
                    here, and it will remain scrollable.</p>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed
                    cursus ante dapibus diam.</p>
                <p>Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec
                    tellus sed augue semper porta.</p>
                <p>Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per
                    conubia nostra, per inceptos himenaeos.</p>
                <p>Curabitur sodales ligula in libero. Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh.
                    Aenean quam.</p>
                <p>In scelerisque sem at dolor. Maecenas mattis. Sed convallis tristique sem. Proin ut ligula vel nunc
                    egestas porttitor.</p>
                <p>Morbi lectus risus, iaculis vel, suscipit quis, luctus non, massa. Fusce ac turpis quis ligula
                    lacinia aliquet. Mauris ipsum.</p>
                <p>Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. Quisque volutpat condimentum
                    velit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
                </p>
            </div>

            <div>
                <div class="input-group mb-3">
                    <div style="width : 100% ; padding : 0px ; margin : 0px">
                        <dropdownWithSearch :options="keywords.map(e => e.word)" width="100%"
                            @newValue="process_keyword" placeholder=" Search or manually add a keyword" />

                    </div>
                </div>
                <div class="keyword-cloud">
                    <span v-for="keyword in keywords" :key="keyword.word" :style="getKeywordStyle(keyword)"
                        @click="selectKeyword(keyword.word)" class="keyword">
                        {{ keyword.word }}
                    </span>
                </div>

            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'KeywordComponent',
    data() {
        return {
            keywords: [
                { "word": "marriage", "related": ["wedding", "joint account", "family planning", "honeymoon"] },
                { "word": "wedding", "related": ["marriage", "honeymoon"] },
                { "word": "honeymoon", "related": ["marriage", "wedding"] },
                { "word": "joint account", "related": ["marriage", "family planning", "bank transfer"] },
                { "word": "family planning", "related": ["marriage", "baby", "joint account"] },

                { "word": "buying a house", "related": ["mortgage", "down payment", "home insurance", "property tax"] },
                { "word": "mortgage", "related": ["buying a house", "interest rates", "home equity loan"] },
                { "word": "down payment", "related": ["buying a house", "car purchase", "savings"] },
                { "word": "home insurance", "related": ["buying a house", "property tax"] },
                { "word": "property tax", "related": ["buying a house", "home insurance"] },

                { "word": "retirement", "related": ["pension", "401k", "investment", "retirement plan"] },
                { "word": "pension", "related": ["retirement", "401k"] },
                { "word": "401k", "related": ["retirement", "pension", "investment"] },
                { "word": "investment", "related": ["retirement", "college", "startup capital"] },
                { "word": "retirement plan", "related": ["retirement", "pension"] },

                { "word": "baby", "related": ["family planning", "childcare", "education fund", "life insurance"] },
                { "word": "childcare", "related": ["baby", "family support"] },
                { "word": "education fund", "related": ["baby", "college", "savings"] },

                { "word": "divorce", "related": ["separation of assets", "child support", "legal fees", "alimony"] },
                { "word": "separation of assets", "related": ["divorce", "inheritance"] },
                { "word": "child support", "related": ["divorce", "baby", "alimony"] },
                { "word": "legal fees", "related": ["divorce", "adoption", "estate planning"] },
                { "word": "alimony", "related": ["divorce", "child support"] },

                { "word": "inheritance", "related": ["estate planning", "will", "trusts", "inheritance tax"] },
                { "word": "estate planning", "related": ["inheritance", "death of spouse", "trusts"] },
                { "word": "will", "related": ["inheritance", "death of spouse"] },
                { "word": "trusts", "related": ["inheritance", "estate planning"] },
                { "word": "inheritance tax", "related": ["inheritance", "gift tax"] },

                { "word": "college", "related": ["student loan", "education fund", "graduation", "scholarships"] },
                { "word": "student loan", "related": ["college", "graduation"] },
                { "word": "scholarships", "related": ["college", "graduation"] },
                { "word": "graduation", "related": ["college", "career planning", "salary expectations"] },

                { "word": "health", "related": ["medical bills", "disability insurance", "health insurance", "life insurance"] },
                { "word": "medical bills", "related": ["health", "insurance"] },
                { "word": "disability insurance", "related": ["health", "life insurance"] },
                { "word": "health insurance", "related": ["health", "medical bills"] },

                { "word": "life insurance", "related": ["baby", "health", "disability insurance", "death of spouse"] },

                { "word": "starting a business", "related": ["business loan", "startup capital", "taxes", "small business account"] },
                { "word": "business loan", "related": ["starting a business", "startup capital"] },
                { "word": "startup capital", "related": ["investment", "starting a business"] },
                { "word": "taxes", "related": ["starting a business", "job change", "gift tax"] },
                { "word": "small business account", "related": ["starting a business"] },

                { "word": "moving", "related": ["relocation loan", "moving expenses", "new job", "cost of living"] },
                { "word": "relocation loan", "related": ["moving", "new job"] },
                { "word": "moving expenses", "related": ["moving", "relocation loan"] },
                { "word": "cost of living", "related": ["moving", "job change"] },

                { "word": "job change", "related": ["salary increase", "severance pay", "tax impact", "cost of living"] },
                { "word": "salary increase", "related": ["job change", "graduation", "career planning"] },
                { "word": "severance pay", "related": ["job change"] },
                { "word": "tax impact", "related": ["job change", "taxes"] },

                { "word": "vacation", "related": ["travel insurance", "savings plan", "credit card rewards", "exchange rate"] },
                { "word": "travel insurance", "related": ["vacation", "health insurance"] },
                { "word": "credit card rewards", "related": ["vacation", "buying a car"] },

                { "word": "car purchase", "related": ["auto loan", "insurance", "down payment", "car trade-in"] },
                { "word": "auto loan", "related": ["car purchase", "interest rates"] },
                { "word": "insurance", "related": ["car purchase", "health", "medical bills"] },
                { "word": "car trade-in", "related": ["car purchase"] },

                { "word": "adoption", "related": ["legal fees", "family support", "education fund"] },
                { "word": "family support", "related": ["adoption", "childcare", "baby"] },

                { "word": "death of spouse", "related": ["will", "life insurance", "survivor benefits", "estate planning"] },
                { "word": "survivor benefits", "related": ["death of spouse", "pension"] },

                { "word": "home renovation", "related": ["home equity loan", "remodeling", "contractor", "personal loan"] },
                { "word": "home equity loan", "related": ["home renovation", "mortgage"] },

                { "word": "large gift", "related": ["gift tax", "bank transfer", "savings", "tax planning"] },
                { "word": "gift tax", "related": ["large gift", "inheritance tax"] },
                { "word": "bank transfer", "related": ["joint account", "large gift"] },

                { "word": "tax planning", "related": ["large gift", "investment", "retirement"] },

                { "word": "personal loan", "related": ["home renovation", "moving expenses"] },
                { "word": "contractor", "related": ["home renovation", "remodeling"] }


            ],
            reload: true,
            selectedKeyword: { word: 'wedding', related: ["marriage", "honeymoon"] }
        }
    },
    mounted() {

        this.keywords = this.keywords.sort(() => Math.random() - 0.5);

    },
    methods: {
        selectKeyword(keyword) {
            this.selectedKeyword = this.keywords.filter(k => k.word == keyword)[0];
            this.reload = false;
            this.reload = true;
        },
        getKeywordStyle(keyword) {
            if (!this.selectedKeyword) return {};

            if (keyword.word === this.selectedKeyword.word) {
                return { fontSize: '24px', fontWeight: 'bold', color: 'var(--c1)' };
            }

            if (this.selectedKeyword.related && this.selectedKeyword.related.includes(keyword.word)) {
                return { fontSize: '18px', fontWeight: '500', color: 'var(--c3)' };
            }

            return { fontSize: '14px', color: 'var(--c3)' };
        },
        process_keyword(keyword) {
            console.log('Processing keyword: ' + keyword);
            if (this.keywords.some(k => k.word === keyword)) {
                console.log("Keyword already exists");
            } else {
                this.keywords.push({ word: keyword, related: [] });
            }

            console.log("Keyword selected: " + keyword);
            this.selectKeyword(keyword)

        }
    },
}

</script>
<style scoped>
#keyword-component {
    position: relative;
}


.windows-content {
    position: relative;
    z-index: 1;


}

h3 {
    margin-right: 20px;
    z-index: 1;
    position: relative;
    text-align: right;

}

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

.windows-content {
    display: flex;
    flex-direction: row;

    height: 100%;
    width: 100%;
}

.windows-content>div {
    flex: 1;
    padding-left : 30px;
    padding-right : 10px;

}

#transcript {
    background-color: rgb(255,255,255, 0.6);
    color: black;
    padding: 10px;
    border-radius: 8px;

    height: 90%;
    width: 50%;
    overflow-y: auto;

}
</style>