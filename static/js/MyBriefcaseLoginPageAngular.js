var myBriefcase = angular.module('myBriefcase',[]);
myBriefcase.controller('myBriefcaseCtrl', function($scope, $http){
	$scope.submit = function()
	{
		var req = {
		 method: 'POST',
		 url: '/user/login/',
		 headers: {
		   'Content-Type': 'application/json'
		 },
		 data: {"username" : $scope.username, "password" : $scope.password}
		}

		$http(req).then(function successCallback(response) {
			// this callback will be called asynchronously
			// when the response is available
		  }, function errorCallback(response) {
			// called asynchronously if an error occurs
			// or server returns response with an error status.
		  });
	}
})