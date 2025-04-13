<script setup>
import dropdownWithSearch from '../blocks/dropdownWithSearch.vue';
import keywordParagraph from '../blocks/keywordParagraph.vue';
</script>
<template>

    <div id="keyword-component" class="windows">

        <div class="windows-content">
            <div id="transcript">
                <p>Chris, great to speak again. I wanted to start with a quick portfolio update. Overall performance
                    declined this quarter due to the
                    <keywordParagraph title="tariff situation" :selected="selectedKeyword" />, but it is outperforming
                    the benchmark. We see some challenges in the tech sector with interest rate expectations and
                    potential increased tariffs.
                </p>

                <p>Thanks for the update. I'm a little concerned about the
                    <keywordParagraph title="tariff situation" :selected="selectedKeyword" /> too, but I believe the
                    technology sector will always grow, regardless of what the experts say. Oh, by the way, how was the
                    <keywordParagraph title="wedding" :selected="selectedKeyword" /> on the honeymoon last month? I hope
                    Simone and you had a great time in Maldives. And anything else new going on in your life here in
                    Zurich?
                </p>

                <p>Yes, we finally got
                    <keywordParagraph title="married" :selected="selectedKeyword" /> and the Maldives were breathtaking.
                    Absolutely stunning. And yes, actually, Simone is pregnant. We're having a baby. We're super
                    excited, but to be honest, a little overwhelmed. We're currently in an apartment and we're thinking
                    about buying a house now.
                </p>

                <p>Oh, that's great. Given this, it may be a wise time to reevaluate your
                    <keywordParagraph title="investment strategy" :selected="selectedKeyword" /> and plan for your
                    <keywordParagraph title="liquidity needs" :selected="selectedKeyword" /> for a home purchase. And
                    just so you know, we have multiple liquidity needs
                    <keywordParagraph title="mortgage" :selected="selectedKeyword" /> offerings when you are ready. We
                    can help with a mortgage pre-approval as well.
                </p>

                <p>Yes, please. That would be a huge help. Also, I have another need. Do you have any other solutions
                    for college
                    <keywordParagraph title="expense planning" :selected="selectedKeyword" /> ? We'll only accept
                    sending our precious and gifted child to Harvard, which is very expensive.
                </p>

                <p>I understand, but no, we don't currently have any dedicated solution on college planning. But let's
                    schedule a follow-up appointment to discuss two other topics. Does Monday afternoon work?</p>

                <p>Monday works perfectly. Thank you, Garrett, for being the world's best advisor.</p>

                <p>You're welcome, Chris. And thank you for being the world's best client.</p>
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
                { "word": "house", "related": ["wedding", "joint account", "family planning"] },
                { "word": "family planning", "related": ['house', 'baby', 'joint account'] },
                { "word": "marriage", "related": ['married', "marriage", "house"] },
                { "word": "college", "related": ["familiy planning"] },
                { "word": "expense planning", "related": ["marriage", "family planning"] },
                { "word": "tariff situation", "related": ["marriage", "baby", "joint account"] },
                { "word": "joint account", "related": ["marriage"] },

                { "word": "mortgage", "related": ["house", "interest rates"] },
                { "word": "liquidity needs", "related": [] },



            ],
            reload: true,
            selectedKeyword:  { "word": "liquidity needs", "related": [] },

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
    padding-left: 30px;
    padding-right: 10px;

}

#transcript {
    background-color: rgb(255, 255, 255, 0.6);
    color: black;
    padding: 10px;
    border-radius: 8px;

    height: 90%;
    width: 50%;
    overflow-y: auto;

}
</style>