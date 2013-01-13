(ns stats-maker.characters)

(def stats [:strength :dexterity :constitution
	:intelligence :wisdom :charisma])

(defn d6 [] (inc (rand-int 6)))

(defn create-score []
	(let [rolls (take 4 (repeatedly d6))
		lowest (apply min rolls)
		score (- (reduce + rolls) lowest)]
	{:score score :rolls rolls}))

(defn gen-character []
	(-> stats
		(zipmap (take 6 (repeatedly create-score)))))
