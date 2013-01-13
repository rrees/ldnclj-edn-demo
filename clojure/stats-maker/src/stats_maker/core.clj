(ns stats-maker.core
	(:require [stats-maker.characters :as chargen])
	(:gen-class))

(defn -main
  [& args]
  (let [characters (take 100 chargen/scores)]
  	(->> characters
  		(apply str)
  		(spit System/out))))
