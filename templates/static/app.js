var vm = new Vue({
  el: '#app',
  data: {
    text: '',
    words: [],
    show: false
  },
  methods: {
    getType: function() {
      this.show = true
      this.words = []

      fetch('/api', {
        method: 'POST',
        body: JSON.stringify({text: this.text}),
        headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json'
        }
      })
        .then(res => res.json())
        .then(data => {
          this.words = data.types
        })
    this.text = ''
      }
    }
})