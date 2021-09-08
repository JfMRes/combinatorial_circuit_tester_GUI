import sys
font=("Arial Bold", 10)

with open(sys.path[0]+'/docs/settings.txt') as f_settings:
    lines=[]
    for line in f_settings:
        lines.append(line)
    def value_setting(ind):
        return lines[ind][lines[ind].index('=')+1:len(lines[ind])-1]
    def_lang=value_setting(0)
    def_timeout=float(value_setting(1))
    def_encode=value_setting(2)
    def_baudrate=int(value_setting(3))
    def_theme=value_setting(4)

with open(sys.path[0]+'/docs/languages/'+def_lang+'.txt') as f_lang:
    lines=[]
    for line in f_lang:
        lines.append(line)
    def value_lang(ind):
        return lines[ind][lines[ind].index('=')+1:len(lines[ind])-1]
    t_error_path=value_lang(0)
    t_error_noinput=value_lang(1)
    t_error_output=value_lang(2)
    t_error_toomanyout=value_lang(3)
    t_error_toomanyin=value_lang(4)
    t_error_noconexion=value_lang(5)
    t_head_main=value_lang(6)
    t_head_debug=value_lang(7)
    t_label_input_pins=value_lang(8)
    t_label_output_pins=value_lang(9)
    t_label_file_path=value_lang(10)
    t_label_time_step=value_lang(11)
    t_button_start=value_lang(12)
    t_button_diagram=value_lang(13)
    t_button_debug=value_lang(14)
    t_button_connect=value_lang(15)
    t_error_no_succes_connction=value_lang(16)


