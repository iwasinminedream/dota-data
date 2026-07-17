// Creating one instance of each known creatable panel type registers its JS
// class with the script system, so the dumper's panel declarations phase
// (cl_panorama_typescript_declarations) can dump real member lists for them.
// The list is the community-verified creatable set (panorama-types
// PanoramaPanelNameMap) plus a few types confirmed by Valve layouts.
(function () {
  var panelTypes = [
    "Panel", "Label",
    "Image", "DOTAAbilityImage", "DOTAItemImage", "DOTAHeroImage", "DOTACountryFlagImage",
    "DOTALeagueImage", "EconItemImage", "AnimatedImageStrip", "DOTAEmoticon",
    "Movie", "DOTAHeroMovie", "DOTAScenePanel", "DOTAParticleScenePanel", "DOTAEconItem",
    "ProgressBar", "CircularProgressBar", "ProgressBarWithMiddle",
    "DOTAUserName", "DOTAUserRichPresence", "DOTAAvatarImage", "Countdown",
    "Button", "TextButton", "ToggleButton", "DOTASettingsCheckbox", "RadioButton",
    "TextEntry", "DOTAHUDShopTextEntry", "NumberEntry", "Slider", "SlottedSlider",
    "RangeSlider", "DropDown", "ContextMenuScript", "Carousel", "DOTAHeroSetList",
    "CarouselNav", "DOTAHUDOverlayMap", "DOTAMinimap", "HTML", "DOTAAccountLinkHTML",
    "DOTAHTMLPanel", "DOTAStoreCustomControls", "CustomLayoutPanel", "TabButton"
  ];
  var host = $.GetContextPanel();
  host.style.visibility = "collapse";
  var created = 0;
  for (var i = 0; i < panelTypes.length; i++) {
    try {
      if ($.CreatePanel(panelTypes[i], host, "")) {
        created++;
      }
    } catch (err) {}
  }
  $.Msg("Dumper: instantiated " + created + " panel types for script class registration");
})();
