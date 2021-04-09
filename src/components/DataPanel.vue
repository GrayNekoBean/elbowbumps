<template>
    <div class="chart-view">
        <Chart type="radar" :data="questionnaireData" />
        <Chart type="bar"   :data="twitterData" />
    </div>
</template>

<script>

export default {
    data(){
        return {
            questionnaireDataSet: [],
            questionnaireData: {
                labels: ['Music', 'Sports', 'Film/TV', 'Video Games', 'Reading', 'Programming'],
                datasets: [
                    {
                        label: "Interests from your questionnaire",
                        backgroundColor: 'rgba(255,99,132,0.2)',
                        borderColor: 'rgba(255,99,132,1)',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: 'rgba(255,99,132,1)',
                        data: this.questionnaireDataSet
                    }
                ]
            },

        }
    }
}
</script>

<style lang="scss" scoped>
.chart-view{
    display: flex;
    justify-content: space-around;
    width: 100%;
}
</style>