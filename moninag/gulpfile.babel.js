import browserify from 'browserify';
import glob from 'glob';
import gulp from 'gulp';
import less from 'gulp-less';
import gutil from 'gulp-util';
import tsify from 'tsify';
import source from 'vinyl-source-stream';


// Convert all .ts fules in one source_app.js file
gulp.task('browserify', () => {
    var files = glob.sync('./static/src/ts/app/**/*.ts');
    return browserify({
            entries: files,
            debug: true
        })
        .plugin(tsify, {
            target: 'es5',
            experimentalDecorators: true
        })
        .bundle()
        .on('error', function(err){
            gutil.log(gutil.colors.red.bold('[browserify error]'));
            gutil.log(err.message);
            this.emit('end');
        })
        .pipe(source('source_app.js'))
        .pipe(gulp.dest('./static/js'));
});

// Convert all .ts fules in one source_app.js file
gulp.task('browserifyAuth', () => {
    var files = glob.sync('./static/src/ts/auth/**/*.ts');
    return browserify({
            entries: files,
            debug: true
        })
        .plugin(tsify, {
            target: 'es5',
            experimentalDecorators: true
        })
        .bundle()
        .on('error', function(err){
            gutil.log(gutil.colors.red.bold('[browserify error]'));
            gutil.log(err.message);
            this.emit('end');
        })
        .pipe(source('auth_app.js'))
        .pipe(gulp.dest('./static/js'));
});

// Copy dependencies to lib folder
gulp.task('copylibs', function() {
    return gulp.src([

            // List here which libs to copy
            'node_modules/rxjs/bundles/Rx.js',
            'node_modules/zone.js/dist/zone.js',
            'node_modules/reflect-metadata/Reflect.js',
        ])
        .pipe(gulp.dest('./static/lib'))
});

// Convert .less to .css
gulp.task('less', function () {
    return gulp.src('./static/src/less/styles.less')
        .pipe(less())
        .on('error', function(err) {
            // Handle less errors, but do not stop watch task
            gutil.log(gutil.colors.red.bold('[Less error]'));
            gutil.log(gutil.colors.bgRed('filename:') +' '+ err.filename);
            gutil.log(gutil.colors.bgRed('lineNumber:') +' '+ err.lineNumber);
            gutil.log(gutil.colors.bgRed('extract:') +' '+ err.extract.join(' '));
            this.emit('end');
        })
        .pipe(gulp.dest('./static/css'))
});

// Watching tasks
gulp.task('watch', () => {
    gulp.watch('./static/src/**/*.ts', ['browserify', 'browserifyAuth']);
    gulp.watch('./static/src/less/*.less', ['less']);
});

// Add build task
gulp.task('build', ['browserify', 'browserifyAuth', 'less', 'copylibs']);

// Add default task
gulp.task('default', ['build', 'watch']);
