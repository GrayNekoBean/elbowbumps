<template>
    <section>
        <Panel>
            <div class="question-div">
            <p class="question-paragraph">
                <slot>Empty Question</slot>
            </p>
            <RadioButton v-for="i in marks" :name="i" :value="i" :key="i" />
            </div>
        </Panel>
    </section>
</template>

<script>
export default {
    data() {
        return {
            marks: [1, 2, 3, 4, 5],
            value: -1,
        }
    }
}
</script>

<style lang="scss">

.question-div {
    position: absolute;
    display: block;    
}

.question-paragraph{
    position: absolute;
    display: block;
    text-align: left;
}

</style>