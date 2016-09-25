var myBriefcase = angular.module('myBriefcase',[]);
myBriefcase.controller('myBriefcaseCtrl', function($scope, $http){
	$http({
		method : "POST",
		url : "/validateLogin",				//API FOR VALIDATING THE CREDENTIALS
		data : {
			"username" : $scope.username,
			"password" : $scope.password
		}.success(function(data){
			if(data.statusCode == "200"){
				console.log("Login Success");
				window.location = "/loginSuccess";	//REQUESTING NEXT PAGE ON SUCCESSSFUL LOGIN
			}
			else{
				alert("Invalid Details");
			}
		})
	})
})