module.exports = function(grunt) {
  require('jit-grunt')(grunt);

  grunt.initConfig({
    less: {
      development: {
        options: {
          compress: false,
          yuicompress: true,
          optimization: 2
        },
        files: {
          './static/css/main.css': './assets/less/main.less'  //destination and src file
        }
      }
    },
    watch: {
      styles: {
        files: ['./assets/less/*.less'], // which files to watch
        tasks: ['less'],
        options: {
          nospawn: true
        }
      }
    }
  });

  grunt.registerTask('default', ['less', 'watch']);
};
