<template>
  <div class="hello">
    <d3-network :net-nodes="nodes" :net-links="links" :options="options" />
  </div>
</template>

<script>
import D3Network from "vue-d3-network";
import letters from "../assets/letters.json";

export default {
  name: "Nodes",
  components: {
    D3Network,
  },
  data() {
    return {
      nodes: [],
      links: [
        /*{ sid: 1, tid: 2 },
         */
      ],
      nodeSize: 10,
      canvas: false,
    };
  },
  methods: {
    createLinks(characters) {
      //complete this code
    },
    getCount(name) {
      var count = 0;
      for (var i = 0; i < letters.length; i++) {
        if (letters[i].to === name) {
          count++;
        }
      }
      return count;
    },
  },
  computed: {
    options() {
      return {
        force: 3000,
        size: { w: 600, h: 600 },
        offset: {
          x: 0,
          y: 0,
        },
        nodeLabels: true,
        linkLabels: true,
        canvas: this.canvas,
      };
    },
  },

  created() {
    let characters = [
      "Chevalier Danceny",
      "Marquise de Merteuil",
      "Cécile Volanges",
      "Présidente de Tourvel",
      "Azolan, chasseur",
      "Madame de Rosemonde",
      "Madame de Volanges",
      "Vicomte de Valmont",
      "Père Anselme",
      "...",
      "M. Bertrand",
      "Anonyme",
      "Sophie Carnay",
      "Maréchale de ***",
      "Le Comte de Gercourt",
    ];

    this.createLinks(characters);

    for (var j = 0; j < characters.length; j++) {
      this.nodes.push({
        id: j,
        name: characters[j],
        _size: this.getCount(characters[j]) + 20,
        _color: "#" + Math.floor(Math.random() * 16777215).toString(16),
      });
    }
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=PT+Sans");
canvas {
  left: 0;
  position: absolute;
  top: 0;
}
.net {
  height: 100%;
  margin: 0;
}
.node {
  -webkit-transition: fill 0.5s ease;
  fill: #dcfaf3;
  transition: fill 0.5s ease;
}
.node.selected {
  stroke: #caa455;
}
.node.pinned {
  stroke: rgba(106, 37, 185, 0.6);
}
.link {
  stroke: rgba(18, 120, 98, 0.3);
}
.link,
.node {
  stroke-linecap: round;
}
.link:hover,
.node:hover {
  stroke: rgba(250, 197, 65, 0.6);
  stroke-width: 5px;
}
.link.selected {
  stroke: rgba(34, 30, 20, 0.6);
}
.curve {
  fill: none;
}
.link-label,
.node-label {
  fill: black;
}
.link-label {
  -webkit-transform: translateY(-0.5em);
  text-anchor: middle;
  transform: translateY(-0.5em);
}

body {
  overflow-x: hidden;
}

body,
html {
  margin: 0;
  padding: 0;
}
body {
  background-color: #fff;
  font-family: "PT Sans";
}

#app {
  bottom: 0;
  left: 0;
  max-width: 100%;
  position: absolute;
  top: 0;
  width: 100%;
}

.links {
  list-style: none;
  margin: 1em 5em 0 0;
  position: absolute;
  right: 0;
  top: 0;
}

#app {
  -moz-user-select: none;
  -ms-user-select: none;
  -webkit-user-select: none;
  text-align: center;
  user-select: none;
}
</style>
