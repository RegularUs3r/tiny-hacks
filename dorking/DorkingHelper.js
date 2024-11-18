function selfloop(i, tosearch) {
     dorking = []
     var x = 1;

     function loop() {
          if (x < i) {
               console.clear()
               console.log(`Loop ${x}`)
               document.getElementById("more-results").click()
               x++
               setTimeout(loop, 5000);
               var links = document.getElementsByTagName('a')
               for (let link = 0; link < links.length; link++) {
                    linko = links[link].getAttribute('href')
                    if (linko != null) {
                         if (linko.includes(tosearch)) {
                              if (linko.startsWith("http")) {
                                   if (!dorking.includes(linko)) {
                                        dorking.push(linko)
                                   }
                              }
                         }
                    }
               }
          }
          dorking.map(links => console.log(links))
     }
     loop()
}selfloop(50)


dorking.map(links => { if (links.includes("contaselect")) { console.log(links) } })