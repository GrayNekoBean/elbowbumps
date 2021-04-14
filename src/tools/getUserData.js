import axios from 'axios';

const getUserData = async (userId, instance) => {
    let address = instance.$store.getters.URL + "user_data";
    let args = {
        user_id: userId
    }
    let userData = null;
    const response = await axios.get(address, {params: args});
    if (response.data.STATUS_CODE == "200"){
        userData = response.data.data;
    }else{
        console.error(response.STATUS);
        console.error(response.Message);
    }
    return userData;
}

export default getUserData;