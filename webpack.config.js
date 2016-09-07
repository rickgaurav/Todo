var webpack = require('webpack');
var path = require('path');

module.exports = {
    context: __dirname,
    devtool: 'eval-source-map',
    entry: './app_todo/static/js/index',
    output: {
        path: path.resolve('./app_todo/static/bundles/'),
        filename: 'bundle.js',
    },

    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loader: 'babel',
                query: {
                    presets: ['es2015', 'react']
                }
            }
        ]
    },

    plugins: [
        new webpack.NoErrorsPlugin()
    ],
    resolve: {
        moduleDirectories: ['node_modules'],
        extensions: ['', '.js', '.jsx']
    }
};