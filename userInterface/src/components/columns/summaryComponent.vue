<template>
    <div>
        <h4>
            Client/Advisor Meeting Notes
        </h4>
        <ul>
            <li>
                Garrett gave an overview of the portfolio performance
            </li>
            <li>
                Haris mentioned multiple life events: getting married, having a baby and planning to purchase a house
            </li>
            <li>
                Garrett mentioned the mortgage services that Raiffeisen offers
            </li>
            <li>
                Haris asked about college planning services
            </li>
        </ul>

        <hr>


        <h4>
            Agreed upon action items
        </h4>

        <ul>
            <li>
                Garrett will schedule a meeting on Monday <br>
                <button type=button class="btn">Schedule a meeting</button>
            </li>
        </ul>
        
        <hr>

        <h4>
            Advisor Suggestions

        </h4>
        <ul>
            <li>
                During the meeting, Haris indicated his confirmation bias regarding technology stocks

            </li>
            <li>
                During the meeting, Haris mentioned a significant life event (getting married). The agent checked the
                client database noting his marital status is single.

            </li>
            <li>
                During the meeting, Haris mentioned a significant life event (having a baby). The Advisor should
                consider updating the portfolio allocation
            </li>

            <li>
                During the meeting, Haris mentioned a significant life event (buying a house). The Advisor should
                consider updating the portfolio allocation to generate liquidity to purchase a house.
            </li>
            <li>
                During the meeting, Haris asked whether Raiffeisen a significant life event (buying a house). The
                Advisor should consider updating the portfolio allocation to generate liquidity to purchase a house.
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: "SummaryComponent",
};
</script>

<style scoped>
* {
    text-align: left;
}

ul {
    text-align: left;
    padding-left: 20px;
}

h4 {
    background-color: transparent;
    color : black ;
}
</style>