<template>
    <div>
        <SplitedPage>
            <template #left>
                <GifPanel></GifPanel>
            </template>
            <template #right>
                <RegisterPanel></RegisterPanel>
            </template>
        </SplitedPage>
    </div>
</template>

<script>
import RegisterPanel from "../components/RegisterPanel";
import SplitedPage from "../components/SplitedPage";
import GifPanel from "../components/GifPanel";

export default {
 components: { RegisterPanel, SplitedPage, GifPanel }
}
</script>

