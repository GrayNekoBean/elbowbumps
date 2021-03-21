<template>
    <div>
        <SplitedPage>
            <template #right>
                <RegisterPanel></RegisterPanel>
            </template>
        </SplitedPage>
    </div>
</template>

<script>
import RegisterPanel from "../components/RegisterPanel";
import SplitedPage from "../components/SplitedPage";

export default {
 components: { RegisterPanel, SplitedPage }
}
</script>
