window.WikiAcad = window.WikiAcad || {}
window.WikiAcad.components = window.WikiAcad.components || {}
window.WikiAcad.components.FollowingMenu = {
	checkDependencies() {
		if( !$.visibility ) {
			console.error("Este módulo requer o plugin Visibility de Semantic UI.")
		}
	},
	start() {
		const $window = $(window)
		const $wrapper = $("#wrapper")
		const $followingBar = $("#menu-bar")
		const $menu = $followingBar.find('.menu')
		const $logo = $followingBar.find('.logo.item img')
		const darkLogo = "/static/images/wiki-v6.png"
		const lightLogo = "/static/images/wiki-v1.png"
		$('body').visibility({
			offset         : -10,
			observeChanges : false,
			once           : false,
			continuous     : false,
			onTopPassed: function() {
				requestAnimationFrame(function() {
					$followingBar.addClass('light fixed')
					$menu.removeClass('inverted')
					$logo.prop('src', darkLogo)
				});
			},
			onTopPassedReverse: function() {
				requestAnimationFrame(function() {
					$followingBar.removeClass('light fixed')
					$menu.addClass('inverted')
					$logo.prop('src', lightLogo)
				})
			}
		})
	}
}