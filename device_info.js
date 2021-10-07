const huaweiLteApi = require('huawei-lte-api');

const connection = new huaweiLteApi.Connection('http://admin:password@192.168.8.1/');

connection.ready.then(function() {
    console.log('Ready');


    const device = new huaweiLteApi.Device(connection);
    device.signal().then(function(result) {
        console.log(result);
    }).catch(function(error) {
        console.log(error);
    });


    device.information().then(function(result) {
        console.log(result);
    }).catch(function(error) {
        console.log(error);
    });

    const dialUp = new huaweiLteApi.DialUp(connection);
    dialUp.setMobileDataswitch(1).then(function(result) {
        console.log(result);
    }).catch(function(error) {
        console.log(error);
    });
});