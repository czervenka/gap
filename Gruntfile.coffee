module.exports = (grunt) ->

    # Project configuration.
    grunt.initConfig
        pkg: grunt.file.readJSON("package.json")
        coffee:
            compile:
                expand: true
                flatten: false
                cwd: 'src/static/coffee'
                src: ['*.coffee']
                dest: 'src/static/js/app'
                ext: '.js'
        watch:
            files: ['src/static/coffee/*.coffee']
            tasks: ['coffee']

    # Load the plugin that provides the "uglify" task.
    grunt.loadNpmTasks("grunt-contrib-coffee")
    grunt.loadNpmTasks("grunt-contrib-watch")

    # Default task(s).
    grunt.registerTask "default", ["coffee"]
