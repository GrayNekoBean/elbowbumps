

var Validation = {
    checkEmail: (email, uomOnly=true) => {
        let pat = '';
        if (uomOnly){
            pat = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@([a-z]+)\.manchester\.ac\.uk$/;
        }else{
            pat = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        }
        let re = new RegExp(pat);
        let res = re.exec(email);
        if (res != null){
            if (res.length > 0){
                return true;
            }
        }
        return false;
    },
    checkName: (userName) => {
        if (userName.length <= 32){
            return true;
        }else{
            return false;
        }
    },
    checkPhoneNumber: (number) => {
        return new RegExp('^[0-9]{8,11}$').test(number);
    }
};

export default Validation;