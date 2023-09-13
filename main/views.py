from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'MC140 Scythe-class Main Battlecruiser',
        'amount': '500~',
        'description': """The MC140 Scythe-class main battle cruiser is the primary warship of the Galactic Alliance, the New Republic's Successor state, in the later half of the century which began with the Battle of Yavin. A Mon Calamari design, the Scythe is unique amongst Mon Calamari designs in focusing
        the majority of its fire power in one direction, akin to the dagger/triangle shaped warships the MC vessel line were originally built to counter. Armed with a slew of heavy energy weapon batteries and a horrifying amount of quick-fire proton torpedo launchers, the Scythe echoes the design philosophy
        of the Victory I Star Destroyer by making use of explosive alpha strikes as its primary damage source, allowing it to handily punch above its size grade against vessels 3 times its size. This came with the drawback also found in triangle shaped vessels in that it was weak to attacks from the rear and
        less suited to broadsides, but with its powerful engines providing plenty of maneuverability and good escort work, such a situation should rarely occur.  The Scythe was so successful that its designers would go on to develop the smaller MC142 Tri-Scythe frigate, which would act like its larger sibling
        on a lesser scale and could often be found escorting it in combat. In this far off future, the Scythe is a sign of the natural evolution of capital ships in the Star Wars galaxy from oversized, resource intensive star dreadnoughts like the Viscount to smaller, more mass producible advanced warships who's
        can cover more space while contesting larger capital ship designs with advanced fire power, a trend typified by Crimson Command nearly a century prior."""
    }

    return render(request, "main.html", context)