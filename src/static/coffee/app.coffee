"use strict"

# Declare app level module which depends on filters, and services
app = angular.module("gap", ['ngRoute'],)

app.config(["$routeProvider", ($routeProvider) ->
    $routeProvider.when "/home",
        templateUrl: "/static/partials/home.html"
        controller: HomeController

    $routeProvider.otherwise(redirectTo: "/home")
])

console.log('App initialized! Hooray!')