
const Validation = {
    checkEmail: (email, uomOnly=true) => {
        let pat = '';
        if (uomOnly){
            pat = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@([a-z]+)\.manchester\.ac\.uk$/;
        }else{
            pat = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        }
        let re = new RegExp(pat);
        return re.test(email);
    },
    checkName: (userName) => {
        if (userName.length <= 32 && userName.length > 0){
            let re = new RegExp(/^[0-9]+.*$/);
            if (!re.test(userName)){
                return true;
            }
        }
        return false;
    },
    checkPhoneNumber: (number) => {
        return new RegExp('^[0-9]{8,11}$').test(number);
    }
};

export default Validation;