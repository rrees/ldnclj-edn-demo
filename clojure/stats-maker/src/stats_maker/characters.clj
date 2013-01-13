(ns stats-maker.characters)

(defn d6 [] (inc (rand-int 6)))

(defn create-score []
	(let [rolls (take 4 (repeatedly d6))
		lowest (apply min rolls)
		score (- (reduce + rolls) lowest)]
	{:score score :rolls rolls}))

(def scores (repeatedly create-score))
