# 1Base

1Base is a project which aims to provide an open source platform for open data.
And just just any data. Lots of data. From various sources.

You can think of 1Base as a wiki for data.

What's more, 1Base is a database of the future. In addition to storing primitive
types (`INTEGER`, `BOOLEAN`, `TEXT`, ...), it stores anything from images to
video to the reason why you walk your dog.

The key here is representations. See the section on <a href="#slot">slots</a>
for more information.

## Basic Premise

![Basic Premise](./doc/images/why.png "Premise")

Let's say you want to build an app that pulls data from an OpenWeather database
and OpenStreetMap database. Currently you have to manage 2 endpoints, and you
have to get 2 different API keys.

And this is already assuming you've been lucky enough to find OpenWeather
and OpenStreetMap as the data provider you need.

If data is gold, and open data is going to change the world, why is it still
fragmented? Shouldn't there be a central place to access it?

## Project Structure


### onebase_common

A library that's used between <a href="#onebase_api">onebase_api</a>
and <a href="onebase_web">onebase_web</a>. Contains common settings and
testing utilities.

Currently the aim is to get 100% JSON output with logging. The typical logging
library has this functionality, but unit tests still use the standard `unittest`
output format.

### onebase_api <a name="onebase_api" />

`onebase_api` is a project for the model infrastructure (what defines the
Nodes, paths, etc.) and the API views. (e.g. `/api/validator/1.0/string`).

In the future the model infrastructure may split off to be its own project.

The API uses [Flask]('https://flask.pocoo.org') as its view framework with
[MongoEngine](http://mongoengine.org/) as the model backend framework.

### onebase_web <a name="onebase_web" />

A pretty (so far, pretty ugly!) front-end to manage user accounts and provide
a graphical, non-API method to manage the 1Base documents.

Like <a href="#onebase_api">onebase_api</a>, it's written in
[Flask]('https://flask.pocoo.org'), but uses HTML templates. onebase_web has
no internal backend, but uses <a href="#onebase_api">onebase_api</a>'s
model backend.

This does need a makeover, so if anyone loves to tinker around with webkits, I'm
welcome to a pretty design.

## Terminology and Methodology

![Description](./doc/images/descrption.png "Description")

### Path

A heirarchical navigation technique to reach a <a href="#node">node</a>.

You can think of a path as a directory structure on a filesystem.

### Key

You can think of a key as a Column on a table. The difference is that a Key
houses a specific Type, and each Type contains a reference to a Validator
and Representer.

Keys are unique to a Node.

### Node <a name="node">

A Node is the backbone to 1Base. It's equivalent to a MySQL table and contains
rows of <a href="#slot">Slots</a>.

Each <a href="#path">Path</a> can contain either 0 or 1 Node, but any number
of paths can point to a node.

Since nodes are heirarchical, they can either be reached by the path name or
by browsing.

### Slot <a name="slot" />

A slot is similar to a MySQL cell (or value), with one uniqure trait: the value
initially returned is not the final value intended to be returned to the user.
Since 1Base can store *any* type of value (including images and audio) this
value is *unrepresented*, and must be passed to a microservice to be represented
to the user.

For example, assume a slot contains the value `https://example.com/image.png`
and the type is `IMAGE`. The value `https://example.com/image.png` is passed
to an API microservice `https://api.example.com/1.0/repr/image/` to grab the
image from the server and write it to the stream.

Before this occurs, however, the slot value needs to be **validated**. A
validator is also--you guessed it--a microservice.

### Source <a name="source" />

You know how on Wikipedia, you must source articles and claims? You must do the
same on 1Base.

A source is simply an acknowledgemnt of the originator of the data. Sources
are loaded into the database using a **method**, which can be one of. The method
can be **externally generated** (a server uploading data to 1Base),
**internally generated** (1Base's own aggregation), or **manually input**
(e.g. from a book text).

Sources can be assigned to a Slot or Node. If a Source is assigned to a Node,
then every Slot within the node inherits the Source.

### Discussion <a name="discussion" />

Sometimes a discrepancy will arise with a document. Like Wikipedia, 1Base
facilitates Discussions between users. Like Sources, Discussions can be assigned
to Nodes and Slots. Discussions can also be assigned to Keys or Sources.

## Getting Involved

I'm hoping this project will evolve into something helpful. So far the major
needs are:

* **Investing.** FLOSS software is awesome but it comes at a price. Please
  consider [Donating on Patreon](https://www.patreon.com/1base).
* **Developers.** Got mad coding skills? Come contribute!
* **Contributed Data.** People hate the sound of crickets. Let's fill this
  sucker up!
