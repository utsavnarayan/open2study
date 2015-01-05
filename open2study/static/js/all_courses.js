var allCourses = [
    {
        title: 'a',
        link: 5,
        ofc: 'a.com'
    },
    {
        title: 'b',
        link: 3,
        ofc: 'b.com'
    },
    {
        title: 'c',
        link: 22,
        ofc: 'c.com'
    },
    {
        title: 'cat',
        link: 32,
        ofc: 'c.com'
    },
    {
        title: 'call',
        link: 42,
        ofc: 'c.com'
    }
    ];

var app = angular.module('courseDetails',[]);

app.factory('fetchAsyncData', function ($http) {
    // Load content using ajax call
    var $apiRoot = "http://localhost:8000/";
    $http.defaults.useXDomain = true;

    function getData(route) {
        return $http({
            url: $apiRoot + route,
            method: "GET"
        });
    };

    return {
        getData: getData
    };
});

app.controller('courses',['$scope', 'fetchAsyncData', function($scope, fetchAsyncData){
    // fetch your data in courses a model in app's scope and can be shared b/w different controllers
    this.searchByTitle = '';
    /*
    Uncomment to fetch data from the py service
    called the function to load data
    fetchAsyncData.getData('index').success(function(result){
        $scope.allCourses = result;// Array JSON similar to static sent from the web service
    });
    */
    this.order = 'title';
    this.reverse = false;
    //comment if using py service data
    $scope.allCourses = allCourses;
    console.log($scope.allCourses);
}]);
