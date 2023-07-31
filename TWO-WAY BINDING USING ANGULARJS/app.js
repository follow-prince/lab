// app.js
angular.module('app', [])
    .controller('FormController', ['$scope', function($scope) {
        $scope.user = {}; // Object to store form data

        $scope.submitForm = function() {
            // Perform form submission logic here
            console.log('Form submitted successfully!');
        };
    }]);
