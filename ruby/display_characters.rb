require 'edn'
require 'curses'

if(ARGV.size() < 1)
	puts "Requires the data file to be passed in"
	exit
end

edn_content = File.read(ARGV[0])

edn_data = EDN.read(edn_content)

#puts edn_data

def init_screen
  Curses.noecho # do not show typed keys
  Curses.init_screen
  Curses.stdscr.keypad(true) # enable arrow keys
  begin
    yield
  ensure
    Curses.close_screen
  end
end

def write(line, column, text)
	Curses.setpos(line, column)
	Curses.addstr(text)
end

def show_character(data)
	inset = 10
	position = 5
	stat_keys = [:strength, :dexterity, :constitution,
		:intelligence, :wisdom, :charisma]

	stat_keys.each_with_index do |key, index|
		write(position + index, inset, key.to_s + " " + data[key][:score].to_s)
	end
end

init_screen do

	index = 0

	loop do
		Curses.clear()

		write(0, 0, "Character display")

		write(1, 2, (index + 1).to_s)

		#write(3, 2, edn_data[index].to_s)

		show_character(edn_data[index])

		case Curses.getch
		when Curses::Key::LEFT then index = [0, index - 1].max
		when Curses::Key::RIGHT then index = [edn_data.size() - 1, index + 1].min

		when ?q then break
		end
	end

end