<template>
    <span :id="textID" class="p-float-label info-text">        
        <div style="margin-right: 5%; margin-top: 5%;"><slot>Text</slot></div>
        <InputText :class="editable ? 'editing' : 'non-editing'" type="text" v-model="text" :disabled="!editable" />
        <div class="edit-button">
            <i class="pi edit-icon" :class="editable ? 'pi-check' : 'pi-pencil'" @click="switchEditable()"></i>
        </div>
    </span>
</template>

<script>
export default {
    props: {
        textID: {
            type: String,
            required: true
        },
        textVar: {
            type: String,
            required: true
        }
    },
    // emits: [
    //     'textVar'
    // ],
    data() {
        return {
            text: this.textVar,
            editable: false
        };
    },
    methods: {
        switchEditable: function(){
            if (this.editable){
                this.$emit('update:textVar', this.text);
            }
            this.editable = !this.editable;
        }
    }
}
</script>

<style lang="scss" scoped>

// ::v-deep{
//     input.p-inputtext{
//         border-top-width: 0px;
//         border-left-width: 0px;
//         border-right-width: 0px;
//         border-bottom-width: 2px;
//         :disabled{
//             border: 0px;
//         }
//     }
// }

.non-editing{
 border-width: 0px;
}

.editing{
    border-top-width: 0px;
    border-left-width: 0px;
    border-right-width: 0px;
    border-bottom-width: 2px;
}

.info-text{
    display: flex;
    justify-content: space-between;
    flex-wrap: nowrap;
    margin: 3%;
    width: 45%;
}

.edit-button{
    margin: 2%;
    :hover{
        border-radius: 50%;
        background: rgba(128, 128, 128, 0.3);
    }
}

.edit-icon{
    padding: 25%;
    height: 2rem;
    width: 2rem;
    cursor: pointer;
}

</style>