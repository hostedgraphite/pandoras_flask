## Pandora's Flask

A worked example of integrating Prometheus monitoring with a Flask app running
in the common `nginx` + `uwsgi` + `Flask` stack.

See the [related blog post](https://www.hostedgraphite.com/blog).

You'll need:
* `nginx` for your platform (we used 1.14.0);
* Python development libraries to build `uWSGI`;
* [virtualenv](https://virtualenv.pypa.io/en/latest/) to build in.

If you want to `make test`, you'll need
[tox](https://tox.readthedocs.io/en/latest/) as well (we used 2.5.0).

Then you should be able to get going with

    make run

Which will start the app running under `nginx` + `uwsgi`.

You can then visit http://localhost:8040/ and look around, or CTRL-C to bring
everything down again.

Once everything's running, you can point a test Prometheus at
http://localhost:9040/metrics to scrape the monitoring data.

Directory layout:
* `bin/` - some helper scripts;
* `conf/` - `nginx` and `uwsgi` configuration;
* `html/` - a simple index for the app;
* `pandoras_flask/` - Python app code;
* `tests/` - simple tests.

[Let us know](mailto:help@hostedgraphite.com) if you run into issues getting
this demo going, or if you find problems in how we've set things up. Thanks!
