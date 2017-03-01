var webpack = require('webpack');
var glob = require('glob');
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var CopyWebpackPlugin = require('copy-webpack-plugin')

var config = {
    resolve: {
        extensions: ['.ts', '.js']
    },

    module: {
        rules: [
            {
              test: /\.ts$/,
              loaders: ['awesome-typescript-loader', 'angular2-template-loader?keepUrl=true'],
              exclude: [/\.(spec|e2e)\.ts$/]
            },

            {
              test: /\.(html|css)$/,
              loader: 'raw-loader',
              exclude: /\.async\.(html|css)$/
            },

            {
              test: /\.async\.(html|css)$/,
              loaders: ['file?name=[name].[hash].[ext]', 'extract']
            },

            {
                test: /\.less$/,
                use: [
                  'style-loader',
                  { loader: 'css-loader', options: { importLoaders: 1 } },
                  'less-loader'
                ]
            },

            {
                test: /.*\.(gif|png|jpe?g|svg)$/i,
                loaders: [
                    {
                        loader: 'file-loader',
                        query: {
                            name: '[name].[ext]',
                            outputPath: '../img/compressed/'
                        }
                    },

                    {
                        loader: 'image-webpack-loader',
                        query: {
                            progressive: true,
                            interlaced: false,
                            pngquant: {
                                quality: '65-70',
                                speed: 4
                            }
                        }
                    }
                ]
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin({filename: './static/css/styles.css',
            allChunks: false
        }),
        new CopyWebpackPlugin([
            { from: 'node_modules/rxjs/bundles/Rx.min.js', to: '../lib' },
            { from: 'node_modules/rxjs/bundles/Rx.min.js.map', to: '../lib' },
            { from: 'node_modules/zone.js/dist/zone.min.js', to: '../lib' },
            { from: 'node_modules/reflect-metadata/Reflect.js', to: '../lib' },
            { from: 'node_modules/reflect-metadata/Reflect.js.map', to: '../lib' },
            { from: 'node_modules/hammerjs/hammer.min.js', to: '../lib' },
            { from: 'node_modules/hammerjs/hammer.min.js.map', to: '../lib' },
        ])
    ]
}

var appConfig = Object.assign({}, config, {
    entry: glob.sync('./static/src/ts/app/**/*.ts'),
    output: {
        path: './static/js',
        filename: 'source_app.js'
    }
});

var authConfig = Object.assign({}, config, {
    entry: glob.sync('./static/src/ts/auth/**/*.ts'),
    output: {
        path: './static/js',
        filename: 'auth_app.js',
        publicPath: './static/img/compressed/'
    }
});

module.exports = [
    appConfig, authConfig
];
