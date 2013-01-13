(ns stats-maker.core
	(:require [stats-maker.characters :as chargen])
	(:gen-class))

(defn -main
  [& args]
  (let [characters (take 100 (repeatedly chargen/gen-character))]
  	(->> characters
  		(apply list)
  		(spit System/out))))
