<template>
    <div>
        <SplitedPage>
            <template #left>
                <GifPanel></GifPanel>
            </template>
            <template #right>
                <LoginPanel></LoginPanel>
            </template>
        </SplitedPage>
    </div>
</template>


<script>
import LoginPanel from "../components/LoginPanel";
import SplitedPage from "../components/SplitedPage";
import GifPanel from "../components/GifPanel";

export default {
 components: { LoginPanel, SplitedPage, GifPanel }
}
</script>
